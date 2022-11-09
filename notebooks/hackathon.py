import json

import httpx


def read_dataset(file="dataset.json"):
    with open(file, "r") as dataset_file:
        return json.load(dataset_file)
    
def read_sample(file="sample.json"):
    with open(file, "r") as sample_file:
        return json.load(sample_file)


def read_proposal(file="proposal.json"):
    with open(file, "r") as proposal_file:
        return json.load(proposal_file)