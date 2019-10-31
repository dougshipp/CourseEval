import {Route} from './route.js'

export class Router {
    constructor()
    {
        this.mode = 'history'
        this.routes = []
        this.root = '/'
    }

    get root(){
        return this._root
    }
    set root(val){
        this._route = val
    }

    get mode(){
        return this._mode
    }
    set mode(val){
        this._mode = (val == 'history' && window.history.pushState) ? 'history' : 'hash'
    }

    get routes()
    {
        return this._routes
    }
    set routes(val)
    {
        this._routes = val
    }

    add(route)
    {
        this.routes.push(new Route(route.name,route.path,route.handler))
    }

    navigate(route)
    {
        route = route ? route : ''
        this.match(route)
    }

    match(route)
    {
        
    }
}