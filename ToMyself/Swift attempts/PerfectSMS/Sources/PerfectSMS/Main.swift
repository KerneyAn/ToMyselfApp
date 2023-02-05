import PerfectHTTP
import PerfectHTTPServer
import Foundation

    var routes = Routes()
    routes.add(method: .post, uri: "/sms", handler: {
        request, response in
        response.setHeader(.contentType, value: "text/xml")
        let body = request.param(name: "Body", defaultValue: "")
        if let bod = body {
            let respStr = "<?xml version=\"1.0\" encoding=\"UTF-8\"?><Response><Message><Body>\(bod)</Body></Message></Response>"
            response.appendBody(string: respStr )
                .completed()
        }
    })

do {
    // Launch the HTTP server.
    try HTTPServer.launch(
        .server(name: "https://971c-169-233-148-89.ngrok.io", port: 8181, routes: routes))
} catch {
    fatalError("\(error)") // fatal error launching one of the servers
}

//public struct PerfectSMS {
    //public private(set) var text = "Hello, World!"

   // public init() {
    //}
//}
