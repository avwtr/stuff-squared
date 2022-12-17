//
//  ContentView.swift
//  trivia
//
//  Created by Alex Vawter on 12/16/22.
//

import SwiftUI

struct ContentView: View {
    @StateObject var triviaManager = TriviaManager()
    
    
    var body: some View {
        NavigationView {
            VStack(spacing:40){
                VStack(spacing: 30){
                    Text("Welcome to The Triviaverse").titleText()
                    Text("Test your knowledge of science").foregroundColor(Color("AccentColor"))
                }
                NavigationLink{
                    triviabridge().environmentObject(TriviaManager())
                }label: {
                    mainbtn(text: "Begin")
                }
                
            
            }.frame(maxWidth: .infinity, maxHeight: .infinity).edgesIgnoringSafeArea(.all)
                .background(Color(red: 0.784 , green: 0.729, blue: 0.847))
        }
    }
}

struct ContentView_Previews: PreviewProvider {
    static var previews: some View {
        ContentView()
    }
}
