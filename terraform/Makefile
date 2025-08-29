.ONESHELL:
.SHELL := /bin/bash
.PHONY: ALL
.DEFAULT_GOAL := fmt

fmt: ## Formats the TF
	terraform fmt -recursive

validate: 
	terraform init && \
	terraform validate 


plan: validate
	terraform plan --out=version

graph:
	terraform graph >> versionplan.svg

apply: plan
	terraform apply -auto-approve 

destroy:
	terraform destroy -auto-approve 

show:
	terraform workspace show
list:
	terraform workspace list
# switch: # make build VERSION=1 if no VERSION then creates with Default
# 	terraform workspace select $(workspace)  || terraform workspace new $(workspace)
