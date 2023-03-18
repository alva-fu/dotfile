# =============== #
# Package: httpgd #
# =============== #

# Disable vscode native plot window
options(vsc.plot = FALSE)

# Show the original httpgd viewer in a webpage in vscode
if (interactive() && Sys.getenv("TERM_PROGRAM") == "vscode") {
  if ("httpgd" %in% .packages(all.available = TRUE)) {
    options(vsc.plot = FALSE)
    options(device = function(...) {
      httpgd::hgd(silent = TRUE)
      .vsc.browser(httpgd::hgd_url(history = FALSE), viewer = "Beside")
    })
  }
}
