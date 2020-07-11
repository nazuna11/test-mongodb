import pymongo
import re

with pymongo.MongoClient("localhost", 27017) as client:
    test_db = client.test_db
    wiskey_collection = test_db.wiskey_collection
    assert wiskey_collection is not None

    # NOTE: insert item
    # wiskey_collection.insert_one({"location": "islay", "name": "caol ila"})

    # NOTE: find item
    #items = wiskey_collection.find({"location": re.compile("ISLAY", re.IGNORECASE)})
    #for item in items:
    #    print(item)

    # NOTE: explain no index
    #explain = wiskey_collection.find({"location": re.compile("ISLAY", re.IGNORECASE)}).explain()
    #print(explain)
    """
    {'queryPlanner': {'plannerVersion': 1, 'namespace': 'test_db.wiskey_collection', 'indexFilterSet': False, 'parsedQuery': {'location': {'$regex': 'ISLAY', '$optio
ns': 'iu'}}, 'winningPlan': {'stage': 'COLLSCAN', 'filter': {'location': {'$regex': 'ISLAY', '$options': 'iu'}}, 'direction': 'forward'}, 'rejectedPlans': []}, '
executionStats': {'executionSuccess': True, 'nReturned': 1, 'executionTimeMillis': 0, 'totalKeysExamined': 0, 'totalDocsExamined': 1, 'executionStages': {'stage'
: 'COLLSCAN', 'filter': {'location': {'$regex': 'ISLAY', '$options': 'iu'}}, 'nReturned': 1, 'executionTimeMillisEstimate': 0, 'works': 3, 'advanced': 1, 'needTi
me': 1, 'needYield': 0, 'saveState': 0, 'restoreState': 0, 'isEOF': 1, 'direction': 'forward', 'docsExamined': 1}, 'allPlansExecution': []}, 'serverInfo': {'host
': 'localhost', 'port': 27017, 'version': '4.2.8', 'gitVersion': 'xxxxxxxxxxxx'}, 'ok': 1.0}
    """

    # NOTE: create index
    #res = wiskey_collection.create_index('location')
    #print(res)

    # NOTE: explain IXSCAN
    #explain = wiskey_collection.find({"location": re.compile("ISLAY", re.IGNORECASE)}).explain()
    #print(explain)
    """
    {'queryPlanner': {'plannerVersion': 1, 'namespace': 'test_db.wiskey_collection', 'indexFilterSet': False, 'parsedQuery': {'location': {'$regex': 'ISLAY', '$optio
ns': 'iu'}}, 'winningPlan': {'stage': 'FETCH', 'inputStage': {'stage': 'IXSCAN', 'filter': {'location': {'$regex': 'ISLAY', '$options': 'iu'}}, 'keyPattern': {'l
ocation': 1}, 'indexName': 'location_1', 'isMultiKey': False, 'multiKeyPaths': {'location': []}, 'isUnique': False, 'isSparse': False, 'isPartial': False, 'index
Version': 2, 'direction': 'forward', 'indexBounds': {'location': ['["", {})', '[/ISLAY/iu, /ISLAY/iu]']}}}, 'rejectedPlans': []}, 'executionStats': {'executionSu
ccess': True, 'nReturned': 1, 'executionTimeMillis': 14, 'totalKeysExamined': 1, 'totalDocsExamined': 1, 'executionStages': {'stage': 'FETCH', 'nReturned': 1, 'e
xecutionTimeMillisEstimate': 0, 'works': 2, 'advanced': 1, 'needTime': 0, 'needYield': 0, 'saveState': 0, 'restoreState': 0, 'isEOF': 1, 'docsExamined': 1, 'alre
adyHasObj': 0, 'inputStage': {'stage': 'IXSCAN', 'filter': {'location': {'$regex': 'ISLAY', '$options': 'iu'}}, 'nReturned': 1, 'executionTimeMillisEstimate': 0,
 'works': 2, 'advanced': 1, 'needTime': 0, 'needYield': 0, 'saveState': 0, 'restoreState': 0, 'isEOF': 1, 'keyPattern': {'location': 1}, 'indexName': 'location_1
', 'isMultiKey': False, 'multiKeyPaths': {'location': []}, 'isUnique': False, 'isSparse': False, 'isPartial': False, 'indexVersion': 2, 'direction': 'forward', '
indexBounds': {'location': ['["", {})', '[/ISLAY/iu, /ISLAY/iu]']}, 'keysExamined': 1, 'seeks': 1, 'dupsTested': 0, 'dupsDropped': 0}}, 'allPlansExecution': []},
 'serverInfo': {'host': 'localhost', 'port': 27017, 'version': '4.2.8', 'gitVersion': 'xxxxxxxxxxxx'}, 'ok': 1.0}
    """

    # NOTE: insert item
    #wiskey_collection.insert_one({"location": "islay", "name": "six isles"})

    # NOTE: explain IXSCAN
    #explain = wiskey_collection.find({"location": re.compile("ISLAY", re.IGNORECASE)}).explain()
    #print(explain)
    """
    {'queryPlanner': {'plannerVersion': 1, 'namespace': 'test_db.wiskey_collection', 'indexFilterSet': False, 'parsedQuery': {'location': {'$regex': 'ISLAY', '$optio
ns': 'iu'}}, 'winningPlan': {'stage': 'FETCH', 'inputStage': {'stage': 'IXSCAN', 'filter': {'location': {'$regex': 'ISLAY', '$options': 'iu'}}, 'keyPattern': {'l
ocation': 1}, 'indexName': 'location_1', 'isMultiKey': False, 'multiKeyPaths': {'location': []}, 'isUnique': False, 'isSparse': False, 'isPartial': False, 'index
Version': 2, 'direction': 'forward', 'indexBounds': {'location': ['["", {})', '[/ISLAY/iu, /ISLAY/iu]']}}}, 'rejectedPlans': []}, 'executionStats': {'executionSu
ccess': True, 'nReturned': 2, 'executionTimeMillis': 0, 'totalKeysExamined': 2, 'totalDocsExamined': 2, 'executionStages': {'stage': 'FETCH', 'nReturned': 2, 'ex
ecutionTimeMillisEstimate': 0, 'works': 3, 'advanced': 2, 'needTime': 0, 'needYield': 0, 'saveState': 0, 'restoreState': 0, 'isEOF': 1, 'docsExamined': 2, 'alrea
dyHasObj': 0, 'inputStage': {'stage': 'IXSCAN', 'filter': {'location': {'$regex': 'ISLAY', '$options': 'iu'}}, 'nReturned': 2, 'executionTimeMillisEstimate': 0,
'works': 3, 'advanced': 2, 'needTime': 0, 'needYield': 0, 'saveState': 0, 'restoreState': 0, 'isEOF': 1, 'keyPattern': {'location': 1}, 'indexName': 'location_1'
, 'isMultiKey': False, 'multiKeyPaths': {'location': []}, 'isUnique': False, 'isSparse': False, 'isPartial': False, 'indexVersion': 2, 'direction': 'forward', 'i
ndexBounds': {'location': ['["", {})', '[/ISLAY/iu, /ISLAY/iu]']}, 'keysExamined': 2, 'seeks': 1, 'dupsTested': 0, 'dupsDropped': 0}}, 'allPlansExecution': []},
'serverInfo': {'host': 'localhost', 'port': 27017, 'version': '4.2.8', 'gitVersion': 'xxxxxxxxxxxx'}, 'ok': 1.0}
    """
