import { NextApiHandler } from "next"
import { connectToDatabase } from "../../../lib/mongodb"
import { PostType } from "../../../type"

const handler : NextApiHandler = async (req, res) => {
    console.log('jdoisjf')
    if(req.method === "GET") {
        const { userId } = req.query as {userId : string}
        try {
            const { db } = await connectToDatabase()

            const Post = db.collection<PostType>("Post")

            const found = await Post.find({userId}, {projection : {_id : 0}}).toArray()
            console.log({found})

            if(!found || !found.length) return res.json({msg : "User not have post.."})

            res.json({data : found})
        }catch(e) {
            return res.status(400).json({msg : e})
        }
    }
}

export default handler 