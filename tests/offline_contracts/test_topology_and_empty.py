"""Closed-curve topology and empty collection conversion boundaries."""

import rhino3dm as r3d
from shapely import geometry

from rhino_shapely_converter import (
    convert_rhino_geometry_to_shapely_geometry as to_shapely,
    convert_shapely_geometry_to_rhino_geometry as to_rhino,
)


def test_closed_3d_linestring_roundtrip_preserves_ring_vertices_and_length():
    source = geometry.LineString([(0, 0, 1), (3, 0, 2), (3, 4, 3), (0, 0, 1)])

    polyline = to_rhino(source)
    converted = to_shapely(polyline)

    assert isinstance(polyline, r3d.Polyline)
    assert polyline.IsClosed
    assert len(polyline) == 4
    assert converted.is_closed
    assert converted.is_ring
    assert list(converted.coords) == list(source.coords)
    assert converted.length == source.length == 12.0


def test_empty_linestring_roundtrips_as_empty_line_geometry():
    source = geometry.LineString()

    polyline = to_rhino(source)
    converted = to_shapely(polyline)

    assert isinstance(polyline, r3d.Polyline)
    assert len(polyline) == 0
    assert converted.geom_type == "LineString"
    assert converted.is_empty
    assert list(converted.coords) == []


def test_empty_shapely_multipoint_converts_to_empty_rhino_pointcloud():
    point_cloud = to_rhino(geometry.MultiPoint([]))

    assert isinstance(point_cloud, r3d.PointCloud)
    assert len(point_cloud) == 0


def test_empty_rhino_pointcloud_converts_to_empty_shapely_multipoint():
    converted = to_shapely(r3d.PointCloud())

    assert isinstance(converted, geometry.MultiPoint)
    assert converted.is_empty
    assert len(converted.geoms) == 0
