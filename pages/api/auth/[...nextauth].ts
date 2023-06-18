import NextAuth from 'next-auth';
import GoogleProvider from 'next-auth/providers/google';
export default NextAuth({
    providers: [
        GoogleProvider({
            clientId: '200118243383-7kfgcb965fnqi19mf0ft9dr11dbqa043.apps.googleusercontent.com',
            clientSecret: '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',
        }),
    ],
    // Optional configuration options
    // ...
});