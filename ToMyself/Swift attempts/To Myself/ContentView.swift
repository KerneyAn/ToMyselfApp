//
//  ContentView.swift
//  To Myself
//
//  Created by Kerney An on 2/4/23.
//

import SwiftUI

struct ContentView: View {
    @State var textFieldText: String = ""

    var body: some View {
        VStack {
            TextField("Enter your name", text: $textFieldText)
                //.textFieldStyle(RoundedBorderTextFieldStyle())
                .padding()
                .background(Color.gray.opacity(0.2).cornerRadius(10))
                .foregroundColor(.gray)
                .font(.headline)
            
            Button(action: {
                
            }, label: {
                Text("Enter")
                    .padding()
                    .background(Color.blue.opacity(0.2).cornerRadius(10))
                    .foregroundColor(.blue)
            })
            }
        }
    }

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
