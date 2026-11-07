# Contributing to NeoBox

A few rules keep the repository consistent.

**Source of truth.** `cad/neobox.blend` is the only geometry source. The STL files, the drawings and every number in the documents are generated or read from it. Never hand-edit an STL. Export with `tools/export_stl.py` and run `tools/verify_stl.py`, which must report all 12 files passing. If you change a published dimension on purpose, update the `EXPECTED` table in the verifier in the same commit.

**Naming in the .blend.** A printed part is named after its STL file. Anything that is not printed carries the `mock_` prefix. The exporter fails on a mesh that is neither, by design.

**Three languages.** README and design exist in English, 简体中文 and 日本語. A change to one is a change to all three, in the same pull request, with the same headings, tables and numbers.

**Claims.** The box has been printed and is in use, but no optical figure has been measured with instruments. Do not write "measured" or "tested" about evenness or flatness.

**Writing.** Say each fact once, in the document where it belongs. Short sentences, tables over prose, no decoration.

Before you open a pull request:

- [ ] `tools/verify_stl.py` passes
- [ ] All three languages updated
- [ ] No new claim of a measurement

Released under the [MIT License](LICENSE).
