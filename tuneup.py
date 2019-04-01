#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tuneup assignment"""

__author__ = "LEllingwood"

import cProfile
import pstats
import timeit


def profile(func):
    """A function that can be used as a decorator to measure performance"""
    def wrapper(*args, **kwargs):
        profile = cProfile.Profile()
        profile.enable()

        result = func(*args, **kwargs)
        profile.disable()
        stats = pstats.Stats(profile)
        stats.sort_stats('cumulative').print_stats(10)
        return result

    return wrapper


def read_movies(src):
    """Read a list of movie titles"""
    print('Reading file: {}'.format(src))
    with open(src, 'r') as f:
        return f.read().splitlines()


def is_duplicate(title, movies):
    """Case insensitive search within a list"""
    return title in movies
    
    # for movie in movies:
        # if movie.lower() == title.lower():
        #     return True
    # return False


@profile
def find_duplicate_movies(src):
    """Returns a list of duplicate movies from a src list"""
    movies = read_movies(src)
    duplicates = []
    while movies:
        movie = movies.pop()
        if is_duplicate(movie, movies):
            duplicates.append(movie)
    return duplicates


def timeit_helper():
    """Part A:  Obtain some profiling measurements using timeit"""
    t = timeit.Timer(stmt="find_duplicate_movies('movies.txt')", setup="from __main__ import find_duplicate_movies")
    t_min = min(t.repeat(repeat=3, number=3))
    print ("Best time across 3 repeats of 3 runs per repeat: {}".format(t_min))


def main():
    """Computes a list of duplicate movie entries"""
    timeit_helper()


if __name__ == '__main__':
    main()
