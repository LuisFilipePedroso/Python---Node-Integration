import express from 'express'
import cors from 'cors'
import axios from 'axios'

class App {

    public express: express.Application

    constructor() {
        this.express = express()
        this.middlewares()
        this.routes()
    }

    private middlewares() : void {
        this.express.use(express.json())
        this.express.use(cors())
    }

    private routes() : void {
        this.express.get('/', async (req, res) => {
            const response = await axios.get('http://localhost:5000')
            console.log(response.data)
            res.send(response.data)
        })
    }
}

export default new App().express