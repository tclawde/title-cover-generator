# Title Cover Generator

Generate beautiful title cover images for social media (Xiaohongshu, etc.)

## Features

- 🎨 Clean note-style design
- 🔤 Large bold fonts
- 📐 9:16 aspect ratio
- ✨ Automatic line breaking
- 🎯 No text overflow

## Quick Start

```bash
pip install Pillow

python3 generate.py "你的标题"
```

## Output

- `/tmp/title_cover.jpg` - Generated cover image

## Requirements

- Python 3.8+
- Pillow
- macOS (uses system fonts)

## Font Support

- STHeiti Medium (default)
- PingFang
- System fallback

## Example

```python
from generate import create_title_cover

# Simple usage
create_title_cover("美院学生都在用AI？我就笑了")

# With subtitle
create_title_cover("美院学生都在用AI？我就笑了", subtitle="AI工具与基本功")
```

## License

MIT
