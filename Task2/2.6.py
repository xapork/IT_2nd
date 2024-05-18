class AirlineCompany:
    planes = []
    routes = []

    def add_aircraft(self, model):
        self.planes.append(model)
        print(self.planes)
        return self.planes

    def remove_aircraft(self, model):
        if model in self.planes:
            self.planes.remove(model)
            print(self.planes)
        return self.planes

    def add_route(self, route):
        self.routes.append(route)
        print(self.routes)
        return self.routes

    def remove_route(self, route):
        if route in self.routes:
            self.routes.remove(route)
            print(self.routes)
        return self.routes

    def search_aircraft(self, model):
        matching_planes = [plane for plane in self.planes if plane == model]
        print(*matching_planes)
        return matching_planes

    def search_route(self, city):
        matching_routes = [route for route in self.routes if city in route]
        print(*matching_routes)
        return matching_routes
airline = AirlineCompany()
airline.add_aircraft('bz')
airline.add_route('a - b')
airline.add_route('d - f')
airline.search_route('d')