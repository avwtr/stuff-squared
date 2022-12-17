//
//  triviabridge.swift
//  trivia
//
//  Created by Alex Vawter on 12/16/22.
//

import SwiftUI

struct triviabridge: View {
    @EnvironmentObject var triviaManager: TriviaManager
    var body: some View {
        
        if triviaManager.reachedEnd {
            VStack(spacing: 20){
                Text("Triviaverse").titleText()
                
                Text("Well done.")
                
                Text("You Scored \(triviaManager.count) out of \(triviaManager.length)")
                
                Button {
                    Task.init {
                        await triviaManager.fetchTrivia()
                    }
                    
                }label: {
                    mainbtn(text: "Let's do it again")
                }
                
            }.foregroundColor(Color("AccentColor")).padding()
                .frame(maxWidth: .infinity, maxHeight: .infinity).background(Color(red: 0.784, green: 0.729, blue: 0.847))
        }else{
            questionV().environmentObject(triviaManager)
        }
        
    }
}

struct triviabridge_Previews: PreviewProvider {
    static var previews: some View {
        triviabridge().environmentObject(TriviaManager())
    }
}



