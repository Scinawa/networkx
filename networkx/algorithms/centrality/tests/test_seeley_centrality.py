#!/usr/bin/env python
import math
from nose import SkipTest
from nose.tools import *
import networkx as nx

class TestSeeleyCentralityDirected(object):
    numpy=1 # nosetests attribute, use nosetests -a 'not numpy' to skip test
    @classmethod
    def setupClass(cls):
        global np
        try:
            import numpy as np
            import scipy
        except ImportError:
            raise SkipTest('SciPy not available.')

    def setUp(self):

        G=nx.DiGraph()

        edges=[(1,2),(1,3),(2,4),(3,2),(3,5),(4,2),(4,5),(4,6),\
               (5,6),(5,7),(5,8),(6,8),(7,1),(7,5),\
               (7,8),(8,6),(8,7)]

        G.add_edges_from(edges,weight=2.0)
        self.G=G.reverse()
        self.G.evc=[0.25368793,  0.19576478,  0.32817092,  0.40430835,
                    0.48199885, 0.15724483,  0.51346196,  0.32475403]

        H=nx.DiGraph()

        edges=[(1,2),(1,3),(2,4),(3,2),(3,5),(4,2),(4,5),(4,6),\
               (5,6),(5,7),(5,8),(6,8),(7,1),(7,5),\
               (7,8),(8,6),(8,7)]

        G.add_edges_from(edges)
        self.H=G.reverse()
        self.H.evc=[0.25368793,  0.19576478,  0.32817092,  0.40430835,
                    0.48199885, 0.15724483,  0.51346196,  0.32475403]


    def test_seeley_centrality_weighted_numpy(self):
        G=self.G
        p=nx.seeley_centrality_numpy(G)
        for (a,b) in zip(list(p.values()),self.G.evc):
            assert_almost_equal(a,b)



    def test_seeley_centrality_unweighted_numpy(self):
        G=self.H
        p=nx.seeley_centrality_numpy(G)
        for (a,b) in zip(list(p.values()),self.G.evc):
            assert_almost_equal(a,b)

class TestSeeleyCentralityExceptions(object):
    numpy=1 # nosetests attribute, use nosetests -a 'not numpy' to skip test
    @classmethod
    def setupClass(cls):
        global np
        try:
            import numpy as np
            import scipy
        except ImportError:
            raise SkipTest('SciPy not available.')
    numpy=1 # nosetests attribute, use nosetests -a 'not numpy' to skip test
    @raises(nx.NetworkXException)
    def test_multigraph(self):
        e = nx.seeley_centrality(nx.MultiGraph())

    @raises(nx.NetworkXException)
    def test_multigraph_numpy(self):
        e = nx.seeley_centrality_numpy(nx.MultiGraph())


    @raises(nx.NetworkXException)
    def test_empty_numpy(self):
        e = nx.seeley_centrality_numpy(nx.Graph())
