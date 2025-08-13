SUBDIRS := $(shell seq -f "D%02g" 1 8) MLGeneral

all:
	@set -e; for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir || exit 1; \
	done

clean:
	@set -e; for dir in $(SUBDIRS); do \
		$(MAKE) -C $$dir clean || exit 1; \
	done

.PHONY: all clean
