import argparse
import datetime
import json

parser = argparse.ArgumentParser()

parser.add_argument(
    "-b", 
    "--begin-date", 
    help="Interval begin date: format date as YYYY-MM-DD.", 
    required=True
)
parser.add_argument(
    "-e", 
    "--end-date", 
    help="Interval end date: format date as YYYY-MM-DD.", 
    required=True
)
parser.add_argument(
    "-n", 
    "--group-number", 
    help="Number of groups to assign", 
    required=True
)
parser.add_argument(
    "-s", 
    "--start-group", 
    help="Number of group to assign on first day", 
    required=True
)
args = parser.parse_args()

class Turni:
    def __init__(self, number_of_groups):
        self.number_of_groups = number_of_groups
        self._init_turni()
        self.delta = datetime.timedelta(days=1)

    def _init_turni(self):
        """
        Inizializza il dizionario principale che ha per chiavi i gruppi.
        """
        self.turni = {}
        for gruppo in range(0, int(self.number_of_groups)):
            turno = {gruppo+1: {}}
            self.turni.update(turno)

    def load(self, start_date, end_date, start_group):
        while start_date <= end_date:
            if not self._has_date_key(start_group, start_date):
                self._add_date_key(start_group, start_date)
            self._add_day(start_group, start_date)
            start_date = self._get_next_date(start_date)
            start_group = self._get_next_group(start_group)

    def _has_date_key(self, target_group, target_date):
        return self._get_date_key(target_date) in self.turni[target_group]

    def _add_date_key(self, target_group, target_date):
        dict_data_key = {self._get_date_key(target_date): []}
        self.turni[target_group].update(dict_data_key)

    def _add_day(self, target_group, target_date):
        days = self.turni[target_group][self._get_date_key(target_date)]
        days.append(target_date.day)
        self.turni[target_group].update({self._get_date_key(target_date): days})

    def _get_date_key(self, target_date):
        return target_date.strftime("%Y-%m")

    def _get_next_date(self, target_date):
        return target_date + self.delta

    def _get_next_group(self, current_group):
        return (current_group % self.number_of_groups) + 1

    def to_json(self, target_path='/tmp/turni.json'):
        fh = open(target_path, 'w')
        fh.write(json.dumps(self.turni))
        fh.close()

start_date = datetime.datetime.strptime(args.begin_date, "%Y-%m-%d")
end_date = datetime.datetime.strptime(args.end_date, "%Y-%m-%d")
number_of_groups = int(args.group_number)
start_group = int(args.start_group)

turni = Turni(number_of_groups)
turni.load(start_date, end_date, start_group)
turni.to_json()