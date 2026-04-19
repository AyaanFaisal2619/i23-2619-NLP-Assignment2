# CS-4063 — Assignment 2: Neural NLP Pipeline

**Student ID:** `i23-2619`  
**Course:** Natural Language Processing (NLP), Assignment 2 — BBC Urdu corpus: distributional representations, sequence tagging, and topic classification.

## Repository layout

| Path | Role |
|------|------|
| `main.ipynb` | End-to-end notebook: Part 1 (TF-IDF, PPMI, Skip-gram), Part 2 (POS/NER + BiLSTM/CRF), Part 3 (Transformer vs BiLSTM topic classification). |
| `part2_seq.py` | Helpers for CoNLL export, lexicons, gazetteer, BiLSTM taggers, CRF training/eval (required for Part 2 cells). |
| `part3_transformer.py` | From-scratch Transformer encoder blocks + topic classifier + BiLSTM baseline, no `nn.Transformer` (required for Part 3 cells). |
| `report.tex` | Written report (Times-like 12pt, 1.5 spacing). Fill numeric macros after training, then compile to PDF. |
| `articles_metadata.json` | Article titles and dates (keys are string article IDs). |
| `cleaned.txt` | Article bodies with `[id]` section markers (used throughout the notebook). |
| `raw.txt` | Raw corpus slice for Skip-gram comparison (Part 1). |

Generated artifacts (created when you run the notebook) typically include `embeddings/`, `data/*.conll`, and `models/*.pt`.

## Environment

Use Python **3.10+** (notebook metadata may list a newer Python; match your local PyTorch build).

```powershell
cd i23-2619-NLP-Assignment2
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install torch numpy scipy scikit-learn matplotlib seaborn tqdm jupyter
```

GPU is optional; the notebook uses `cuda` when available.

## Running the work

1. Place `cleaned.txt`, `raw.txt`, and `articles_metadata.json` in the project root (same folder as `main.ipynb`).  
2. Open `main.ipynb` and run cells **from the top in order** so shared objects exist (`vocab`, `emb_c3`, `meta`, `DATA_DIR`, etc.).  
3. Part 3 assumes Part 1 Skip-gram (condition **C3**, `d=100`) has been trained so `emb_c3` and `vocab` are defined.  
4. After Part 3 evaluation cells, copy **test accuracy** and **macro-F1** for the Transformer and BiLSTM topic baseline into `report.tex` (see macros below).

> **Note:** This repo’s `.gitignore` may exclude large `.txt` / `.npy` files. For submission, follow your instructor’s packaging rules (e.g. zip notebook + code + PDF report + any required data paths).

## Report (PDF)

1. Edit the macros at the top of `report.tex`: set `\GithubURL` to your real repository URL and paste numeric results into `\TransTestAcc`, `\TransMacroF`, `\LstmTestAcc`, `\LstmMacroF` (plain text, e.g. `0.812` or `81.2\%` style is fine).  
2. Compile twice if you use cross-references:

   ```powershell
   pdflatex -interaction=nonstopmode report.tex
   pdflatex -interaction=nonstopmode report.tex
   ```

Install a LaTeX distribution if needed (e.g. [MiKTeX](https://miktex.org/) or TeX Live). The report targets **12pt**, **1.5 line spacing**, and a short structure: Overview → Part 1–3 results → Conclusion.

## GitHub

Replace the placeholder in `report.tex` and optionally add your remote:

```text
https://github.com/<YOUR_USERNAME>/i23-2619-NLP-Assignment2
```

## Course submission ZIP (roll **i23-2619**)

Use your instructor’s **DS section** code (examples below use `DS-1`; replace `1` with your section digit if needed).

| Item | Requirement |
|------|-------------|
| **Zip file name** | `i23-2619_Assignment2_DS-<section>.zip` (e.g. `i23-2619_Assignment2_DS-1.zip`) |
| **Root folder inside zip** | `i23-2619_Assignment2_DS-<section>\` (must match the zip stem) |
| **Notebook** | `i23-2619_Assignment2_DS-<section>.ipynb` — **all cells executed** (rename from `main.ipynb` when packaging) |
| **Report** | `report.pdf` only — **Times New Roman 12pt**, **1.5 line spacing**, **2–3 pages**, sections: **Overview**, **Part 1 Results**, **Part 2 Results**, **Part 3 Results**, **Conclusion**. Do **not** submit `.md` / `.docx` as the report. |
| **`embeddings/`** | `tfidf_matrix.npy`, `ppmi_matrix.npy`, `embeddings_w2v.npy`, `word2idx.json` |
| **`models/`** | `bilstm_pos.pt`, `bilstm_ner.pt`, `transformer_cls.pt` |
| **`data/`** | `pos_train.conll`, `pos_test.conll`, `ner_train.conll`, `ner_test.conll` |

Validation CoNLL files (`*_val.conll`) are **not** listed in the brief; they stay in your repo for local training but **omit them from the submission zip** unless the LMS explicitly asks for them.

### Automated zip (Windows)

1. Run the full `main.ipynb` (save with outputs).  
2. Compile `report.tex` → `report.pdf` in the project root.  
3. From this folder in PowerShell:

   ```powershell
   .\make_submission_zip.ps1          # default section DS-1
   .\make_submission_zip.ps1 -Section 3   # -> ..._DS-3.zip
   ```

The script copies `main.ipynb` to the required notebook name inside the zip and bundles only the paths in the table above.

## Licence

See `LICENSE` in the repository root (if present).
