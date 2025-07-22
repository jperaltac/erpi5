SUBDIRS := $(shell seq -f "D%02g" 1 10)

all:
	@for dir in $(SUBDIRS); do \
	$(MAKE) -C $$dir; \
	done

clean:
	@for dir in $(SUBDIRS); do \
	$(MAKE) -C $$dir clean; \
	done

.PHONY: all clean
