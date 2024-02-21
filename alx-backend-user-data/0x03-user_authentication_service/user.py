#!/usr/bin/env python3
"""
Module for creating user database
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class User(Base):
    """
    Creates/TRepresents table for users
    """
