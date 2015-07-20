'''
libChEBIpy (c) University of Manchester 2015

libChEBIpy is licensed under the MIT License.

To view a copy of this license, visit <http://opensource.org/licenses/MIT/>.

@author:  neilswainston
'''
from libchebipy._base_object import BaseObject

class Structure(BaseObject):
    '''COMMENT'''

    def __init__(self, structure, typ, dimension):
        self.__structure__ = structure
        self.__typ__ = typ
        self.__dimension__ = dimension
        BaseObject.__init__(self)


    def get_structure(self):
        '''Returns structure'''
        return self.__structure__


    def get_type(self):
        '''Returns type'''
        return self.__typ__


    def get_dimension(self):
        '''Returns dimension'''
        return self.__dimension__


class StructureType(object):
    '''COMMENT'''
    InChIKey = 0
    mol = 1
    SMILES = 2
