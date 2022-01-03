include .env
export

mkfile_path := $(abspath $(lastword $(MAKEFILE_LIST)))
current_dir := $(notdir $(patsubst %/,%,$(dir $(mkfile_path))))
ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

PROJECT_DIR=edw

configs:
	echo $(ROOT_DIR)
	echo $(PROJECT_DIR)
	echo ${TARGET_DBT}

docs:
	cd $(PROJECT_DIR);~/.local/bin/dbt docs generate --profiles-dir $(ROOT_DIR)/$(PROJECT_DIR) --target ${TARGET_DBT}

web:
	cd $(PROJECT_DIR);~/.local/bin/dbt docs serve --profiles-dir $(ROOT_DIR)/$(PROJECT_DIR) --target ${TARGET_DBT}

deploy:
	cd $(PROJECT_DIR);~/.local/bin/dbt run --profiles-dir $(ROOT_DIR)/$(PROJECT_DIR) --target ${TARGET_DBT}

test:
	cd $(PROJECT_DIR);~/.local/bin/dbt test --profiles-dir $(ROOT_DIR)/$(PROJECT_DIR) --target ${TARGET_DBT}