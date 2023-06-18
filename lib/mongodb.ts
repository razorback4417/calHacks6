import { MongoClient, MongoClientOptions, Db } from 'mongodb';

let cachedClient: MongoClient | undefined;
let cachedDb: Db | undefined;

export async function connectToDatabase(): Promise<{ client: MongoClient; db: Db }> {
  if (cachedClient && cachedDb) {
    return { client: cachedClient, db: cachedDb };
  }

  const uri = process.env.MONGODB_URI;
  const options: MongoClientOptions = {};

  if (!uri) {
    throw new Error('MONGODB_URI environment variable is not defined.');
  }

  const client = new MongoClient(uri, options);
  await client.connect();
  const db = client.db();

  cachedClient = client;
  cachedDb = db;

  return { client, db };
}
