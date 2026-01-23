# Git Local Branches Report

Generated on: 23 de janeiro de 2026

## Summary

There are 5 local branches in the repository. The current active branch is **upm/mini-m4**.

Two branches (`2025-09-23-code-review` and `upm/mini-m4`) are pointing to the same latest commit, suggesting they are in sync or duplicates for different tracking purposes.

## Branch Details

| Branch Name | Commit | Upstream | Last Updated | Commit Message |
|:---|:---|:---|:---|:---|
| **upm/mini-m4** (current) | `2a175e4` | `origin/upm/mini-m4` | 2025-09-12 | Code review (location_analysis). filename uniformization |
| 2025-09-23-code-review | `2a175e4` | `origin/2025-09-23-code-review` | 2025-09-12 | Code review (location_analysis). filename uniformization |
| main | `730c752` | `origin/main` | 2025-08-15 | Local de entrada de Estêvão Lopes |
| master | `6fb3982` | `origin/master` | 2025-06-12 | Update notebooks |
| temp | `6ee0d4f` | - | 2025-06-09 | Entry related references |

## Observations

1. **Active Development**: 
   - `upm/mini-m4` and `2025-09-23-code-review` contain the most recent work (Sept 2025).
   - They share the exact same commit hash (`2a175e4`), indicating identical content.

2. **Mainline Branches**:
   - `main` is behind the current development branches (Last update: Aug 2025).
   - `master` appears to be older (Last update: June 2025). Having both `main` and `master` often happens during migration of default branch names; verify which is the intended default.

3. **Stale/Temporary Branches**:
   - `temp` has no upstream tracking and hasn't been updated since June 2025. It might be a candidate for deletion if the experiments in "Entry related references" are no longer needed.
