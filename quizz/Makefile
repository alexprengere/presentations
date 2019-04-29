
TARGETS = slides.html

RSTS5 = rst2s5.py
RM = rm

#RSTFLAGS = --theme=small-black

# Make all
all: $(TARGETS)

# Suffices rules
.SUFFIXES: .rst .html

.rst.html:
	@($(RSTS5) $(RSTFLAGS) $< $@ && echo "$@ is generated.")

clean:
	@($(RM) $(TARGETS))
	@echo "All HTML files are deleted !"
