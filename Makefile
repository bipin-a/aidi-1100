# Variables
VENV_DIR = venv
PYTHON = python
REQUIREMENTS = requirements.txt

# Targets
.PHONY: help venv install activate clean

# Show help menu
help:
	@echo "Usage: make <target>"
	@echo "Targets:"
	@echo "  venv       - Create virtual environment"
	@echo "  install    - Install dependencies from requirements.txt"
	@echo "  activate   - Activate the virtual environment"
	@echo "  clean      - Remove virtual environment"

# Create virtual environment
venv:
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created in $(VENV_DIR)"

# Install dependencies from requirements.txt
install: venv
	$(VENV_DIR)/bin/pip install --upgrade pip
	$(VENV_DIR)/bin/pip install -r $(REQUIREMENTS)
	@echo "Dependencies installed from $(REQUIREMENTS)"

# Activate virtual environment (for Unix-like systems)
activate:
	@echo "Run 'source $(VENV_DIR)/bin/activate' to activate the virtual environment"

# Clean up (remove virtual environment)
clean:
	rm -rf $(VENV_DIR)
	@echo "Virtual environment removed"

