"""
.. module:: chronological
   :synopsis: Manipulation and formatting of dates.
.. moduleauthor:: Benardi <github.com/Benardi>
"""

from dateutil import parser


def conform_date(date):

   """Enforce data to specific format.

    Conform datestring to typical brazilian format.

    :param str date: Date string .

    :return: Date in  in 'dd/mm/yyyy hh:mm:ss' format 

    :rtype: str
    """
   time = parser.parse(date)
   formatted = time.strftime('%d/%m/%Y %H:%M:%S')
   return formatted