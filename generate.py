#!/usr/bin/env python3
"""
Title Cover Generator v1.0

Generate clean, bold title cover images for social media.

Usage:
    python3 generate.py "你的标题"
    python3 generate.py "标题" "副标题"
    python3 generate.py "标题" --output /path/to/output.jpg
"""

import os
from PIL import Image, ImageDraw, ImageFont

# Configuration
DEFAULT_SIZE = (900, 1600)  # 9:16 aspect ratio
DEFAULT_BG = (255, 248, 220)  # Light yellow note paper
DEFAULT_TEXT = (0, 0, 0)  # Black
DEFAULT_ACCENT = (200, 50, 50)  # Red
DEFAULT_FONT_SIZE = 90
DEFAULT_MARGIN = 120


def find_font(size: int = DEFAULT_FONT_SIZE):
    """Find available CJK font"""
    font_paths = [
        "/System/Library/Fonts/STHeiti Medium.ttc",
        "/System/Library/Fonts/PingFang.ttc",
        "/System/Library/Fonts/STHeiti Light.ttc",
        "/System/Library/Fonts/Helvetica.ttc",
    ]
    
    for fp in font_paths:
        if os.path.exists(fp):
            try:
                return ImageFont.truetype(fp, size)
            except:
                continue
    
    return ImageFont.load_default()


def create_title_cover(
    title: str,
    subtitle: str = "",
    output_path: str = "/tmp/title_cover.jpg",
    font_size: int = DEFAULT_FONT_SIZE,
    bg_color: tuple = DEFAULT_BG,
    text_color: tuple = DEFAULT_TEXT,
    accent_color: tuple = DEFAULT_ACCENT,
):
    """
    Generate a title cover image.
    
    Args:
        title: Main title text
        subtitle: Optional subtitle
        output_path: Output file path
        font_size: Font size (default 90)
        bg_color: Background color RGB
        text_color: Text color RGB
        accent_color: Accent color RGB
    
    Returns:
        output_path
    """
    width, height = DEFAULT_SIZE
    
    # Create image
    img = Image.new('RGB', (width, height), color=bg_color)
    draw = ImageDraw.Draw(img)
    
    # Draw paper lines
    for i in range(140, height - 100, 45):
        draw.line([(100, i), (width - 50, i)], fill=(240, 235, 220), width=2)
    
    # Draw left red line
    draw.line([(90, 110), (90, height - 110)], fill=accent_color, width=5)
    
    # Load font
    font = find_font(font_size)
    
    # Smart line breaking
    lines = []
    current = ""
    
    for char in title:
        test_line = current + char
        left, top, right, bottom = font.getbbox(test_line)
        text_width = right - left
        
        if text_width <= width - DEFAULT_MARGIN * 2:
            current = test_line
        else:
            if current:
                lines.append(current)
            current = char
    
    if current:
        lines.append(current)
    
    # Draw title
    y = height // 3
    for i, line in enumerate(lines):
        left, top, right, bottom = font.getbbox(line)
        text_width = right - left
        x = (width - text_width) / 2
        draw.text([x, y + i * (font_size + 15)], line, font=font, fill=text_color)
    
    # Draw subtitle
    if subtitle:
        sub_y = y + len(lines) * (font_size + 20) + 60
        subtitle_text = f"「{subtitle}」"
        left, top, right, bottom = font.getbbox(subtitle_text)
        sub_width = right - left
        sub_x = (width - sub_width) / 2
        draw.text([sub_x, sub_y], subtitle_text, font=font, fill=text_color)
    
    # 保存
    img.save(output_path, quality=90, optimize=True)
    print(f"✅ Cover: {output_path} ({len(lines)} lines)")
    
    return output_path


def main():
    """CLI entry point"""
    import sys
    
    if len(sys.argv) < 2:
        print("Usage: python3 generate.py \"标题\" [副标题]")
        print("Example: python3 generate.py \"美院学生都在用AI？我就笑了\"")
        sys.exit(1)
    
    title = sys.argv[1]
    subtitle = sys.argv[2] if len(sys.argv) > 2 else ""
    
    create_title_cover(title, subtitle)


if __name__ == "__main__":
    main()
