# Review notes

- Original archive included a nested `GitAction.zip` containing a `.git`
  directory and Git history. It has intentionally been excluded from this
  prepared source bundle; inspect and sanitize its history separately if it is
  needed.
- macOS `__MACOSX` metadata and `.DS_Store` files are excluded.
- Hard-coded Google Apps Script deployment URLs have been replaced with
  `GOOGLE_APPS_SCRIPT_URL` configuration in scripts that used them.
- The supplied paper describes YOLO/MobileNetV2/trajectory regression, but those
  components are not present in the top-level scripts from the supplied ZIP.
- Dataset provenance, paper-to-code mapping, tests, and project license remain
  unresolved. Do not claim this draft reproduces paper results.
