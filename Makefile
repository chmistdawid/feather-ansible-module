.PHONY: test

test:
	ANSIBLE_LIBRARY=./src ansible-playbook test/playbook.yml