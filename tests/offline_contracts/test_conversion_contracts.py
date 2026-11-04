import pytest
import shapely.geometry as geom
from rhino_shapely_converter import (
    convert_shapely_geometry_to_rhino_geometry as to_rhino,
)
from rhino_shapely_converter import (
    convert_rhino_geometry_to_shapely_geometry as to_shapely,
)


@pytest.mark.parametrize("coordinates", [(1.25, -2.5), (1.25, -2.5, 3.75)])
def test_point_conversion_expected_coordinates_and_z_default(coordinates):
    result = to_rhino(geom.Point(coordinates))
    assert (result.X, result.Y, result.Z) == (
        coordinates[0],
        coordinates[1],
        coordinates[2] if len(coordinates) == 3 else 0,
    )
    shape = to_shapely(result)
    assert tuple(shape.coords[0]) == (
        coordinates[0],
        coordinates[1],
        coordinates[2] if len(coordinates) == 3 else 0,
    )


def test_polyline_roundtrip_preserves_vertices_and_length():
    shape = geom.LineString([(0, 0, 0), (3, 0, 0), (3, 4, 0)])
    result = to_shapely(to_rhino(shape))
    assert list(result.coords) == [(0, 0, 0), (3, 0, 0), (3, 4, 0)]
    assert result.length == 7


def test_geometry_conversion_rejects_unsupported_types():
    with pytest.raises(ValueError):
        to_rhino(geom.Polygon([(0, 0), (1, 0), (0, 1)]))
    with pytest.raises(ValueError):
        to_shapely(object())
