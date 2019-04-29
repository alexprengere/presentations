
TARGETS = slides.html

RSTS5 = landslide
RSTFLAGS = -o

RM = rm

# Make all
all: $(TARGETS)

# Suffices rules
.SUFFIXES: .rst .html

.rst.html:
	@($(RSTS5) $(RSTFLAGS) $< > $@ && echo "$@ is generated.")

clean:
	@($(RM) $(TARGETS))
	@echo "All HTML files are deleted !"
