import numpy as np
from math import *


def perspective_mat(angle_of_view, aspect_ratio, near_plane, far_plane):
    a = radians(angle_of_view)
    d = 1.0 / tan(a/2)
    r = aspect_ratio
    b = (near_plane + far_plane) / (near_plane - far_plane)
    c = far_plane * near_plane / (near_plane - far_plane)

    # transposed version

    return np.array(
        [
            [d/r, 0, 0, 0],
            [0, d, 0, 0],
            [0, 0, b, c],
            [0, 0, -1, 1],
        ],
        np.float32
    )


def ortho_mat(left, right, top, bottom, near, far):
    return np.array(
        [
            [2 / (right - left), 0, 0, -(right + left) / (right - left)],
            [0, 2 / (top - bottom), 0, -(top + bottom) / (top - bottom)],
            [0, 0, -2/(far - near), -(far + near) / (far - near)],
            [0, 0, 0, 1],
        ],
        np.float32
    )


def identity_mat():
    return np.array(
        [
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ],
        np.float32
    )


def translate_mat(x, y, z):
    return np.array(
        [
            [1, 0, 0, x],
            [0, 1, 0, y],
            [0, 0, 1, z],
            [0, 0, 0, 1],
        ],
        np.float32
    )


def scale_mat3(x, y, z):
    return np.array(
        [
            [x, 0, 0, 0],
            [0, y, 0, 0],
            [0, 0, z, 0],
            [0, 0, 0, 1],
        ],
        np.float32
    )


def scale_mat(s):
    return np.array(
        [
            [s, 0, 0, 0],
            [0, s, 0, 0],
            [0, 0, s, 0],
            [0, 0, 0, 1],
        ],
        np.float32
    )


def rotate_x_mat(angle):
    t = radians(angle)
    a, b = sin(t), cos(t)

    return np.array(
        [
            [1, 0, 0, 0],
            [0, b, -a, 0],
            [0, a, b, 0],
            [0, 0, 0, 1],
        ],
        np.float32
    )


def rotate_y_mat(angle):
    t = radians(angle)
    a, b = sin(t), cos(t)

    return np.array(
        [
            [b, 0, a, 0],
            [0, 1, 0, 0],
            [-a, 0, b, 0],
            [0, 0, 0, 1],
        ],
        np.float32
    )


def rotate_z_mat(angle):
    t = radians(angle)
    a, b = sin(t), cos(t)

    return np.array(
        [
            [b, -a, 0, 0],
            [a, b, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ],
        np.float32
    )


def rotate_a_mat(angle, axis):
    t = radians(angle)
    s, c = sin(t), cos(t)

    axis = axis.normalize()
    ux2 = axis.x*axis.x
    uy2 = axis.y*axis.y
    uz2 = axis.z*axis.z

    return np.array(
        [
            [c + (1-c)*ux2, (1-c)*axis.y*axis.x - s*axis.z,
             (1-c)*axis.z*axis.x + s*axis.y, 0],
            [(1-c)*axis.y*axis.x + s*axis.z, c+(1-c) *
             uy2, (1-c)*axis.z*axis.y - s*axis.x, 0],
            [(1-c)*axis.x*axis.z - s*axis.y, (1-c) *
             axis.y*axis.z + s*axis.x, c+(1-c)*uz2, 0],
            [0, 0, 0, 1]
        ],
        np.float32
    )

    return np.array(
        [
            [b, -a, 0, 0],
            [a, b, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1],
        ],
        np.float32
    )


def translate(m, x, y, z):
    return m @ translate_mat(x, y, z)


def scale3(m, x, y, z):
    return m @ scale_mat3(x, y, z)


def scale(m, s):
    return m @ scale_mat(s)


def rotate_x(m, angle, local=True):
    t = rotate_x_mat(angle)
    return m @ t if local else t @ m


def rotate_y(m, angle, local=True):
    t = rotate_y_mat(angle)
    return m @ t if local else t @ m


def rotate_z(m, angle, local=True):
    t = rotate_z_mat(angle)
    return m @ t if local else t @ m


def rotate_a(m, angle, axis, local=True):
    t = rotate_a_mat(angle, axis)
    return m @ t if local else t @ m
