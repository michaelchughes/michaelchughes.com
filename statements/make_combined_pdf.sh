export PAPERS_DIR=$HOME/git/michaelchughes/content/papers/

gs \
    -sDEVICE=pdfwrite -dCompatibilityLevel=1.4 -dPDFSETTINGS=/default \
    -dNOPAUSE -dQUIET -dBATCH -dDetectDuplicateImages \
    -dCompressFonts=true -r10 \
    -sOutputFile=/tmp/merged.pdf \
    $PAPERS_DIR/HughesSudderth_NIPS_2013.pdf \
    $PAPERS_DIR/HughesStephensonSudderth_NIPS_2015.pdf \
    $PAPERS_DIR/HughesElibolMcCoyPerlisDoshi_MLHCWorkshopAtNIPS2016.pdf

