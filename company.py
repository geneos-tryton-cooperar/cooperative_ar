from trytond.model import ModelView, ModelSQL, fields
from trytond.pyson import Bool, Eval
from trytond.pool import Pool, PoolMeta

__all__ = ['Company']
__metaclass__ = PoolMeta

class Company:    
    __name__ = 'company.company'

    numero_matricula = fields.Char('Numero de Matricula')
    responsable_administrativo = fields.Many2One('party.party', 'Responsable Administrativo', required=True)