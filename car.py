class Car:
    def __init__(
            self, license, brand, model, lp100,
            cost_per_hour, cost_per_day, cost_per_week
    ):
        self.license = license
        self.brand = brand
        self.model = model
        self.lp100 = lp100
        self.cost_per_hour = cost_per_hour
        self.cost_per_day = cost_per_day
        self.cost_per_week = cost_per_week

    @classmethod
    def from_dict(cls, dict):
        return cls(
            dict[ 'license' ], dict[ 'brand' ], dict[ 'model' ],
            dict[ 'lp100' ], dict[ 'cost_per_hour' ],
            dict[ 'cost_per_day' ], dict[ 'cost_per_week' ]
        )

    def __repr__(self):
        return self.license
