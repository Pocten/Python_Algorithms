class Vertex:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.minDistance = float('inf')
        self.previousVertex = None
        self.delete = 0
        self.edges = []
        self.path = []


class Edge:
    def __init__(self, source, target, weight):
        self.source = source
        self.target = target
        self.weight = weight


class Dijkstra:
    def __init__(self):
        self.count = 0
        self.edgesToVertexes = []
        self.vertexes = []
        self.unvisitedVertexes = list()
        self.visitedVertexes = []
        self.start = False

    def getMinimum(self, array):
        minimum = Vertex('a', 'tmp')
        minimum.minDistance = float('inf')
        for item in self.vertexes:
            if (item.minDistance <= minimum.minDistance) and (item.id not in array):
                minimum = item
        return minimum

    def computePath(self, sourceId):
        self.start = sourceId
        visit = []
        visited = []
        for item in self.vertexes:
            if item.id == sourceId:
                item.minDistance = 0
                item.previousVertex = sourceId
            visit.append(item.id)

        while len(visited) != len(visit):
            start = self.getMinimum(visited)

            for edge in start.edges:
                end = self.getVertex(edge.target)
                way = start.minDistance + edge.weight
                if end.minDistance >= way:
                    end.previousVertex = start.id
                    end.minDistance = way
            visited.append(start.id)

    def getShortestPathTo(self, targetId):
        way = []
        tmp = self.getVertex(targetId)
        way.insert(0, tmp)
        while tmp.previousVertex != tmp.id:
            tmp = self.getVertex(tmp.previousVertex)
            if tmp is None:
                break
            way.insert(0, tmp)
        return way

    def getVertex(self, vertex_id):
        vertex = None
        for item in self.vertexes:
            if item.id == vertex_id:
                vertex = item
                break
        return vertex

    def createGraph(self, vertexes, edgesToVertexes):
        self.vertexes = vertexes
        self.edgesToVertexes = edgesToVertexes
        for vert1 in vertexes:
            for edge1 in edgesToVertexes:
                if vert1.id == edge1.source:
                    vert1.edges.append(edge1)

    def resetDijkstra(self):
        self.count = 0
        for currentVertex in self.vertexes:
            currentVertex.delete = 0
            currentVertex.minDistance = float('inf')
            currentVertex.previousVertex = None

    def getVertexes(self):
        return self.vertexes

