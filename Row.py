class Row():
    def __init__(self,r):
        try:
            self.game_ID = r[0]
            self.INST_ID=r[1]
            self.period=r[2]
            self.clock=r[3]
            self.home_team=r[4]
            self. home_score=r[5]
            self.home_fgm=r[6]
            self.home_fga=r[7]
            self.away_team=r[8]
            self.away_score=r[9]
            self.away_fgm=r[10]
            self.away_fga=r[11]
            self.away_ps_line=r[12]
            self.away_ps_odd=r[13]
            self.over_line=r[14]
            self.over_odd=r[15]
            self.home_ps_line=r[16]
            self.home_ps_odd=r[17]
            self.under_line=r[18]
            self.under_odd=r[19]
            self.away_ml_odd=r[20]
            self.home_ml_odd=r[21]
        except:
            print(r)