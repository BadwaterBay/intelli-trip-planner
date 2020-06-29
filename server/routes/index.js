import express from 'express';

const router = express.Router();

/* GET users listing. */
router.get('/', (req, res, next) => {
  res.send('Success! The server is running.');
});

export default router;
