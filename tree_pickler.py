import pickle # standard library 

interview_header = ["level", "lang", "tweets", "phd"]
interview_tree = ['Attribute', 'level', ['Value', 'Junior', 
                                            ['Attribute', 'phd', 
                                                ['Value', 'yes', 
                                                    ['Leaf', 'False', 2, 5]], 
                                                ['Value', 'no', 
                                                    ['Leaf', 'True', 3, 5]]]], 
                                        ['Value', 'Mid', 
                                            ['Leaf', 'True', 4, 14]], 
                                        ['Value', 'Senior', 
                                            ['Attribute', 'tweets', 
                                                ['Value', 'yes', 
                                                    ['Leaf', 'True', 2, 5]], 
                                                ['Value', 'no', 
                                                    ['Leaf', 'False', 3, 5]]]]]

# pickle (object serialization): saving binary representation of an object (eg the tree)
#   to a file for loading and using later
# example: saving a trained model for inference/prediction later
#   in another python process, possibly running on a diff machine (server)
# imagine: just trained an awesome MyRandomForestClassifier
#   now you need to save it for using in your web app on a server later
# de/un-pickle (object deserialization): loading a binary representation of an object
#   from a file into a python object in memory 
# example: a web app that loads the trained model up for inference/prediction requests from clients

# let's pickle the header and tree (together)
packaged_obj = (interview_header, interview_tree)
# wb: binary write mode
outfile = open("tree.p", "wb")
pickle.dump(packaged_obj, outfile)
# tree.p is in binary so we can't read it
outfile.close()
