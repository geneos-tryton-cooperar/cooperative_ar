from trytond.pool import Pool
from .partner import *
from .meeting import *
from .vacation import *
from .partnermeeting import *
from .sanction import *
from .recibo import *
from .account import *
from .company import *


def register():
    Pool.register(Partner,
                  Meeting,
                  Vacation,
                  PartnerMeeting,
                  Sanction,
                  Recibo,
                  FiscalYear,
                  Company,
                  module='cooperative_ar', type_='model'
                  )
    Pool.register(
        ReciboReport,
        module='cooperative_ar', type_='report')
