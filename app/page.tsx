'use client';

import { useState, useEffect } from 'react';

const TARGET_ADDRESS = "0x32b9Cb68c3CF4e046C7a19A3147e076e8D064476";
const GUARDIAN_ADDRESS = "0xFc832406Ae1De8af6FacF35f2ebaeD6dC84F6288";

export default function AegisHaltDashboard() {
  const [isSandbox, setIsSandbox] = useState(false);
  const [loading, setLoading] = useState(false);
  const [targetStatus, setTargetStatus] = useState('ACTIVE');
  const [haltLogs, setHaltLogs] = useState<string[]>([]);

  useEffect(() => {
    // Simulated check to determine if the GenLayer RPC is reachable from Vercel
    const checkNetwork = async () => {
      const rpcOk = false; // Set to true if integrating genlayer-js for live web reading
      setIsSandbox(!rpcOk);
    };
    checkNetwork();
  }, []);

  const triggerGuardianHalt = async () => {
    setLoading(true);
    
    if (isSandbox) {
      // Sandbox Mode: Simulate the Guardian AI evaluating a threat and halting the Target
      setTimeout(() => {
        setHaltLogs(prev => [
          ...prev, 
          "[AI GUARDIAN] Threat detected in mempool payload.",
          "[AI GUARDIAN] Consensus reached: HALT.",
          `[TARGET: ${TARGET_ADDRESS}] State locked successfully.`
        ]);
        setTargetStatus('HALTED');
        setLoading(false);
      }, 2000);
    } else {
      // Live integration via genlayer-js would go here
      try {
        setTargetStatus('HALTED');
      } catch (e: any) {
        setHaltLogs(prev => [...prev, `Error: ${e.message}`]);
      }
      setLoading(false);
    }
  };

  return (
    <main className="min-h-screen bg-slate-900 text-slate-100 py-12 px-4 font-mono">
      <div className="max-w-4xl mx-auto space-y-8">
        <header className="border-b border-slate-700 pb-6">
          <h1 className="text-3xl font-bold text-emerald-400">AegisHalt Protocol</h1>
          <p className="text-slate-400 mt-2">Autonomous AI Guardian & Emergency Target Pause</p>
        </header>

        {isSandbox && (
          <div className="bg-amber-900/50 border border-amber-500/50 text-amber-200 p-4 rounded-md text-sm">
            ⚠️ <strong>Network Fallback Active:</strong> Vercel cannot reach local RPC. Running in Sandbox Mode for UI verification.
          </div>
        )}

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          {/* Target Contract Panel */}
          <div className="bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-xl">
            <h2 className="text-lg font-semibold text-slate-300 mb-4">Target Contract</h2>
            <div className="space-y-4">
              <div>
                <div className="text-xs text-slate-500 uppercase">Deployment Address (Bradbury Testnet)</div>
                <div className="text-sm break-all">{TARGET_ADDRESS}</div>
              </div>
              <div>
                <div className="text-xs text-slate-500 uppercase">Current State</div>
                <div className={`text-xl font-bold mt-1 ${targetStatus === 'ACTIVE' ? 'text-emerald-400' : 'text-rose-500'}`}>
                  {targetStatus}
                </div>
              </div>
            </div>
          </div>

          {/* Guardian Control Panel */}
          <div className="bg-slate-800 p-6 rounded-lg border border-slate-700 shadow-xl flex flex-col justify-between">
            <div>
              <h2 className="text-lg font-semibold text-slate-300 mb-4">Guardian Node</h2>
              <div className="text-xs text-slate-500 uppercase mb-1">Deployment Address (Bradbury Testnet)</div>
              <div className="text-sm break-all mb-6">{GUARDIAN_ADDRESS}</div>
            </div>
            
            <button 
              onClick={triggerGuardianHalt}
              disabled={loading || targetStatus === 'HALTED'}
              className="w-full bg-rose-600 hover:bg-rose-700 disabled:bg-slate-700 text-white font-bold py-3 px-4 rounded transition-colors"
            >
              {loading ? 'Evaluating Threat...' : targetStatus === 'HALTED' ? 'Protocol Halted' : 'Simulate Threat / Trigger Halt'}
            </button>
          </div>
        </div>

        {/* Execution Logs */}
        <div className="bg-black p-4 rounded-lg border border-slate-800 min-h-[150px]">
          <div className="text-xs text-slate-500 uppercase mb-2">Guardian Execution Logs</div>
          {haltLogs.length === 0 ? (
            <div className="text-slate-600 text-sm">Awaiting execution...</div>
          ) : (
            <ul className="space-y-1">
              {haltLogs.map((log, i) => (
                <li key={i} className="text-sm text-emerald-300 flex gap-2">
                  <span className="text-slate-600">&gt;</span> {log}
                </li>
              ))}
            </ul>
          )}
        </div>
      </div>
    </main>
  );
}
