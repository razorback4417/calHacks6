import { NextApiResponse } from "next";
import nc from "next-connect";
import { connectToDatabase } from "../../../lib/mongodb";
import { PostType } from "../../../type";

const handler = nc({
  onError(err, _, res: NextApiResponse) {
    res.status(400).json({ msg: "Something Went Wrong.." });
  },
});

handler.get(async (_, res: NextApiResponse) => {
  console.log('yo')
  const { db } = await connectToDatabase();
  console.log(db);
  const Post = db.collection<PostType>("Post");
  const Posts = await Post.find({}, { projection: { _id: 0 } }).toArray();
  console.log(Posts)
  res.json({ post: Posts });

  return;
});

export default handler;
