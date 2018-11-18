import json


def openCollection(path):
    # Opening collection json
    with open(path, 'r') as f:
        postman_collection = json.load(f)

    postman_collection_info = postman_collection["info"]

    print("Name of collection is: " + str(postman_collection_info["name"]))

    # Name of collection
    postman_collection_items = postman_collection["item"]

    # list of tests
    for item in postman_collection_items:
        if item["name"] == "Auth: Digest":
            for item2 in item["item"]:
                if item2["name"] == "DigestAuth Request":
                    print(item2["name"])
                    print(item2["event"][0]["script"]["exec"])


def openEnvironment(path):
    # Opening environment json
    with open(path, 'r') as f:
        postman_environment = json.load(f)

    # Name of environment
    print("Name of environment is: " + postman_environment["name"])

    for item in postman_environment["values"]:
        print(item["key"] + " has value: " + item["value"])

    # Change var3
    for item in postman_environment["values"]:
        if item["key"] == "Var3":
            item["value"] = "Changed"

    # Write out to tmp.json file
    with open('tmp.json', 'w') as outfile:
     json.dump(postman_environment, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)


openCollection('data/postman_collections/echo.json')
#openEnvironment('data/Test.postman_environment.json')