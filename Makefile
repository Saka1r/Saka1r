.PHONY: banner preview purge

banner:
	python3 tools/build_banner.py

preview:
	grip -b README.md

purge:
	curl -X PURGE "$(CAMO_URL)"
