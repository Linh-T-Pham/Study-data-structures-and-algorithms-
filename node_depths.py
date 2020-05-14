"""
   the distance between a node in a Binary Tree and the tree's root is called 
   the node's depth. Write a function that takes in a Binary Tree and returns
   the sum of its nodes' depths. 

   Each Binary Tree node has an integer value, a left child node and a right
   child node. Children nodes can either be BinaryTree nodes themselves or
   None / null. 



    {
        "tree": {
        "nodes": [
        {"id": "1", "left": "2", "right": "3", "value": 1},
        {"id": "2", "left": "4", "right": "5", "value": 2},
        {"id": "3", "left": "6", "right": "7", "value": 3},
        {"id": "4", "left": "8", "right": "9", "value": 4},
        {"id": "5", "left": null, "right": null, "value": 5},
        {"id": "6", "left": null, "right": null, "value": 6},
        {"id": "7", "left": null, "right": null, "value": 7},
        {"id": "8", "left": null, "right": null, "value": 8},
        {"id": "9", "left": null, "right": null, "value": 9}
        ],
        "root": "1"
        }
    }


    {
        "tree": {
        "nodes": [
            {"id": "1", "left": "2", "right": null, "value": 1},
            {"id": "2", "left": null, "right": null, "value": 2}
            ],
        "root": "1"
        }
    }
       
"""
















if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED. HOORAY!\n")