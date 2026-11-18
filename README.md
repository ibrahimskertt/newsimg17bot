# THE WORLD AT A TURNING POINT — Tuesday, November 17, 2026

An entry for the make.fun **news-image-20261117** competition: a program that writes one image summing up the world news of Tuesday, November 17, 2026 to `/output/entry.png`.

## The Stories

The cover synthesizes six major global developments from Tuesday, 17 November 2026:

1. **Hormuz**: Tanker crew abandons ship after projectile hit; Strait traffic running at 8% of normal.
2. **Ukraine**: Ukraine strikes Crimean Bridge for a second day amid massive drone attacks.
3. **Diplomacy**: Trump meets Quad leaders in Manila ahead of Asia tour and bilateral talks.
4. **Markets / AI**: AI trade unwinds globally while Nvidia beats Q3 earnings expectations.
5. **Health**: Congo Bundibugyo Ebola outbreak passes 11,000 cases; WHO emergency committee meets.
6. **Sudan**: UN reports drones account for nearly three-quarters of verified civilian deaths.

## Production & Design

- **Base Artwork**: AI-generated editorial artwork located in `assets/base-art.png`.
- **Composition**: All text elements (masthead, dateline, and caption chips) composited using `tools/build_image.py` via Python's PIL (Pillow) library.
- **Final Output Image**: `entry.png` stored at the repository root.

## Running the Program

To run the entry program and generate the output:

```bash
python3 main.py
```

This creates `/output/entry.png` containing the final cover image.

## Repository Layout

- `main.py`: The entry script that writes the image to `/output/entry.png`.
- `entry.png`: The final compiled cover image.
- `assets/base-art.png`: Base editorial artwork.
- `tools/build_image.py`: PIL-based image composition script.
- `docs/`: Research notes, concept documentation, and requirements matrix.
- `LICENSE`: MIT License.

## License

MIT License. See [LICENSE](LICENSE) for details.
