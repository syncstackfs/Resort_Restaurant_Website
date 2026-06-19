"""Optional image compression for Vercel deploy builds (requires Pillow)."""
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    Image = None

STATIC_IMAGES = Path(__file__).resolve().parent.parent / "msresort" / "static" / "images"
MAX_WIDTH = 1400
JPEG_QUALITY = 82


def optimize_image(path: Path) -> None:
    original_size = path.stat().st_size
    suffix = path.suffix.lower()

    with Image.open(path) as img:
        if img.width > MAX_WIDTH:
            ratio = MAX_WIDTH / img.width
            new_size = (MAX_WIDTH, int(img.height * ratio))
            img = img.resize(new_size, Image.Resampling.LANCZOS)

        if suffix in (".jpg", ".jpeg"):
            rgb = img.convert("RGB")
            rgb.save(path, "JPEG", quality=JPEG_QUALITY, optimize=True)
        elif suffix == ".png":
            img.save(path, "PNG", optimize=True)
        elif suffix == ".webp":
            img.save(path, "WEBP", quality=JPEG_QUALITY, method=6)
        elif suffix == ".avif":
            return

    saved = original_size - path.stat().st_size
    if saved > 0:
        print(f"  {path.name}: {original_size // 1024}KB -> {path.stat().st_size // 1024}KB")


def main() -> None:
    if Image is None:
        print("Pillow not installed — skipping image optimization.")
        return

    if not STATIC_IMAGES.is_dir():
        raise SystemExit(f"Missing images directory: {STATIC_IMAGES}")

    print(f"Optimizing images in {STATIC_IMAGES}")
    for path in sorted(STATIC_IMAGES.iterdir()):
        if path.suffix.lower() in (".jpg", ".jpeg", ".png", ".webp"):
            try:
                optimize_image(path)
            except OSError as exc:
                print(f"  Skipped {path.name}: {exc}")
    print("Done.")


if __name__ == "__main__":
    main()
