const {getData} = require('../scripts/ExperimentData.js');

const express = require('express');
const User = require('../models/user');
const bcrypt = require('bcryptjs');
const router = express.Router();
var timeStart,timeDone;
router.get('/experimentdata', (req, res) => {
    var data = getData();
    const d = new Date();
    const seconds = 1000 * 60 * 60;
    timeStart = Date.now();
    res.send(data);
  });

router.post('/register', async (req, res) => {
    // We will be passing the data to this API in JSON format. The Express server makes it available inside the 
    // req.body object.

    const d = new Date();
    const seconds = 1000 * 60 * 60;
    timeDone = Date.now();
    var timeTaken=Math.floor((timeDone - timeStart) / 1000);
    try {
        // we pass all the user data (like first_name, last_name, age, gender, country, state and city)
        // which is present in the req.body to the User constructor 
        user = new User(req.body);
		user.time_taken = timeTaken;
        // save all the details along with hashed password into the MongoDB database.
        await user.save();
        // Once we're done, we're sending back the response with the status code of 201 which describes that 
        // something has been created.
        res.status(201).send();
    } catch (e) {
        res.status(500).send('Something went wrong. Try again later.');
    }
});

// we're exporting the express router so we can use it in the index.js file.
module.exports = router;