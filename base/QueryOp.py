"""
QueryOp.py ~ github.com/nokusukun
Provides pythonic bindings to MongoDB's Query Operators
"""

"""
Name    Description
$eq     Matches values that are equal to a specified value.
$gt     Matches values that are greater than a specified value.
$gte    Matches values that are greater than or equal to a specified value.
$in     Matches any of the values specified in an array.
$lt     Matches values that are less than a specified value.
$lte    Matches values that are less than or equal to a specified value.
$ne     Matches all values that are not equal to a specified value.
$nin    Matches none of the values specified in an array.
"""
Equal           = lambda x : {"$eq" : x}
GreaterThan     = lambda x : {"$gt" : x}
GreaterEqual    = lambda x : {"$gte" : x}
In              = lambda x : {"$in" : x}
LessThan        = lambda x : {"$lt" : x}
LessEqual       = lambda x : {"$lte" : x}
NotEqual        = lambda x : {"$ne" : x}
NotEqualIn      = lambda x : {"$nin" : x}


"""
Logical

Name    Description
$and    Joins query clauses with a logical AND returns all documents that match the conditions of both clauses.
$not    Inverts the effect of a query expression and returns documents that do not match the query expression.
$nor    Joins query clauses with a logical NOR returns all documents that fail to match both clauses.
$or Joins query clauses with a logical OR returns all documents that match the conditions of either clause.
"""
And             = lambda x : {"$and" : x}
Not             = lambda x : {"$not" : x}
Nor             = lambda x : {"$nor" : x}
Or              = lambda x : {"$or" : x}


"""
Element

Name    Description
$exists Matches documents that have the specified field.
$type   Selects documents if a field is of the specified type.
"""
Exists          = lambda x : {"$exists" : x}
Type            = lambda x : {"$type" : x}


"""
Evaluation

Name    Description
$mod    Performs a modulo operation on the value of a field and selects documents with a specified result.
$regex  Selects documents where values match a specified regular expression.
$text   Performs text search.
$where  Matches documents that satisfy a JavaScript expression.
"""
Mod             = lambda x : {"$mod" : x}
Regex           = lambda x : {"$regex" : x}
Text            = lambda x : {"$text" : x}
Where           = lambda x : {"$where" : x}

"""
Geospatial

Name    Description
$geoIntersects  Selects geometries that intersect with a GeoJSON geometry. The 2dsphere index supports $geoIntersects.
$geoWithin  Selects geometries within a bounding GeoJSON geometry. The 2dsphere and 2d indexes support $geoWithin.
$near   Returns geospatial objects in proximity to a point. Requires a geospatial index. The 2dsphere and 2d indexes support $near.
$nearSphere Returns geospatial objects in proximity to a point on a sphere. Requires a geospatial index. The 2dsphere and 2d indexes support $nearSphere.
"""

"""
Array

Name        Description
$all        Matches arrays that contain all elements specified in the query.
$elemMatch  Selects documents if element in the array field matches all the specified $elemMatch conditions.
$size       Selects documents if the array field is a specified size.
"""
All         = lambda x : {"$all" : x}
ElemMatch   = lambda x : {"$elemMatch" : x}
Size        = lambda x : {"$size" : x}

"""
Bitwise

Name    Description
$bitsAllClear   Matches numeric or binary values in which a set of bit positions all have a value of 0.
$bitsAllSet Matches numeric or binary values in which a set of bit positions all have a value of 1.
$bitsAnyClear   Matches numeric or binary values in which any bit from a set of bit positions has a value of 0.
$bitsAnySet Matches numeric or binary values in which any bit from a set of bit positions has a value of 1.
"""