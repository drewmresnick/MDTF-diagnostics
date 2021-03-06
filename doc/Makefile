# Minimal makefile for Sphinx documentation

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
PAPER         = letter

# Internal variables.
PAPEROPT_a4     = -D latex_elements.papersize=a4
PAPEROPT_letter = -D latex_elements.papersize=letter
ALLSPHINXOPTS   = -d $(BUILDDIR)/doctrees $(PAPEROPT_$(PAPER)) $(SPHINXOPTS) .

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help clean clean_all html dirhtml singlehtml latex latexpdf text man changes linkcheck Makefile

clean:
	-rm -rf $(BUILDDIR)/*

clean_all:
	-rm -rf $(BUILDDIR)
	-rm -rf sphinx_pods
	-rm -rf sphinx_sites
	-rm sphinx/src.*

html:
	$(SPHINXBUILD) -v -T -E -b html $(ALLSPHINXOPTS) $(BUILDDIR)/html
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/html."

dirhtml:
	$(SPHINXBUILD) -b dirhtml $(ALLSPHINXOPTS) $(BUILDDIR)/dirhtml
	@echo
	@echo "Build finished. The HTML pages are in $(BUILDDIR)/dirhtml."

singlehtml:
	$(SPHINXBUILD) -b singlehtml $(ALLSPHINXOPTS) $(BUILDDIR)/singlehtml
	@echo
	@echo "Build finished. The HTML page is in $(BUILDDIR)/singlehtml."

latex:
	$(SPHINXBUILD) -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo
	@echo "Build finished; the LaTeX files are in $(BUILDDIR)/latex."
	@echo "Run \`make' in that directory to run these through (pdf)latex" \
	      "(use \`make latexpdf' here to do that automatically)."

latexpdf:
	$(SPHINXBUILD) -v -T -E -b latex $(ALLSPHINXOPTS) $(BUILDDIR)/latex
	@echo "Running LaTeX files through pdflatex..."
	make -C $(BUILDDIR)/latex all-pdf
	@echo "pdflatex finished; the PDF files are in $(BUILDDIR)/latex."
	-cp -f _build/latex/MDTF_getting_started.pdf _static/MDTF_getting_started.pdf
	-cp -f _build/latex/MDTF_walkthrough.pdf _static/MDTF_walkthrough.pdf
	@echo "Copied PDFs to _static."

text:
	$(SPHINXBUILD) -b text $(ALLSPHINXOPTS) $(BUILDDIR)/text
	@echo
	@echo "Build finished. The text files are in $(BUILDDIR)/text."

changes:
	$(SPHINXBUILD) -b changes $(ALLSPHINXOPTS) $(BUILDDIR)/changes
	@echo
	@echo "The overview file is in $(BUILDDIR)/changes."

linkcheck:
	$(SPHINXBUILD) -b linkcheck $(ALLSPHINXOPTS) $(BUILDDIR)/linkcheck
	@echo
	@echo "Link check complete; look for any errors in the above output " \
	      "or in $(BUILDDIR)/linkcheck/output.txt."

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
#	@sphinx-apidoc -f --separate --no-toc --output-dir "./sphinx" "../src"
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
